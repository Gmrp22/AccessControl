from rest_framework import viewsets, status
from rest_framework.response import Response
from datetime import date
# Models
from QR.models.access import Access
from QR.models.user import User
from QR.models.report import Report
# Serializer
from QR.serializers.access import AccessSerializer
from time import time
import datetime as dt


class AccessViewSet(viewsets.ModelViewSet):
    queryset = Access.objects.all()

    def get_serializer_class(self):
        """Define serializer"""
        return AccessSerializer

    def create(self, request):
        """Manage access"""
        serializer = AccessSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            flag = False
            try:
                access = Access.objects.filter(
                    user=user).get(date=date.today())
                if access.status == 'IN':
                    access.status = 'OUT'
                    access.save()
                    flag = True
                    self.daily_report(flag, user, access)
                    return Response({"Acceso diario": "Salida"}, status=status.HTTP_201_CREATED)
            except:
                access_new = Access(status='IN', user=user)
                access_new.save()
                return Response({"Acceso diario": "Ingreso"}, status=status.HTTP_201_CREATED)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def daily_report(self, flag, user, access):
        if flag == True:
            try:
                # Se revisa si existe un reporte semanal
                report = Report.objects.filter(
                    user=user).get(status="Open")
                # Se revisa cuantos reportes se tienen
                print(".------------------------------SE TIEN REPORTE")
                if report.count < 6:
                    # No se ha terminado la semana
                    print(".-----------------------------No se ha terminado la semana")
                    worked = access.departure_time.hour - access.entry_time.hour
                    self.extra_hours(report, worked)

                    # Se ha terminado la semana
                else:
                    worked = access.departure_time.hour - access.entry_time.hour
                    self.extra_hoursClosed(report, worked)
            except:
                print(".------------------------------CREANDO REPORTE")
                # Si no existe un reporte semanal se crea
                worked = access.departure_time.hour - access.entry_time.hour

                self.report_creation(worked, user)

                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def extra_hours(self, report, worked):
        if worked > 8:
            extra = worked-8
            report.count = report.count + 1
            report.worked = report.worked + 8
            report.extra = report.extra + extra
            report.save()
        else:
            # Si no hay
            report.count = report.count + 1
            report.worked = report.worked + worked
            report.extra = 0
            report.save()

    def extra_hoursClosed(self, report, worked):
        if worked > 8:
            extra = worked-8
            report.count = report.count + 1
            report.worked = report.worked + 8
            report.extra = report.extra + extra
            report.status = "Closed"
            report.save()
        else:
            # Si no hay
            report.count = report.count + 1
            report.worked = report.worked + worked
            report.status = "Closed"
            report.extra = 0
            report.save()

    def report_creation(self, worked, user):
        if worked > 8:
            extra = worked-8
            report = Report(count=1, user=user, worked=8, extra=extra)
            report.save()
            # Si hay horas extra
        else:
            # Si no hay
            report = Report(count=1, user=user, worked=worked, extra=0)
            report.save()
