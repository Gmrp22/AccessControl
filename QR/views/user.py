from datetime import date
from rest_framework import viewsets, status
from rest_framework.response import Response
import qrcode
# Models
from QR.models.user import User
from QR.models.qr import QR
from QR.models.access import Access
from QR.models.report import Report
# Serializer
from QR.serializers.user import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        """Define serializer"""
        return UserSerializer

    def create(self, request):
        """User creation"""
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            img = qrcode.make(new_user.carnet)
            f = open("QRTemp/output" + new_user.carnet + ".png", "wb")
            img.save(f)
            f.close()
            new_QR = QR(image="QRTemp/output" +
                        new_user.carnet + ".png", user=new_user)
            new_QR.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def update(self, request, pk):
    #     """Manage access"""
    #     user = User.objects.get(pk=pk)
    #     try:
    #         access = Access.objects.filter(user=user).get(date=date.today())
    #         if access.status == 'IN':
    #             access.status = 'OUT'
    #             access.save()
    #             return Response(status=status.HTTP_201_CREATED)
    #         else:
    #             return Response(status=status.HTTP_400_BAD_REQUEST)
    #     except:
    #         access_new = Access(status='IN', user=user)
    #         access_new.save()
    #         return Response(status=status.HTTP_201_CREATED)
    #     return Response(status=status.HTTP_400_BAD_REQUEST)

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

    def update(self, request, pk):
        """Manage access"""
        user = User.objects.get(pk=pk)
        flag = False
        try:
            access = Access.objects.filter(user=user).get(date=date.today())
            if access.status == 'IN':
                access.status = 'OUT'
                access.save()
                flag = True
        except:
            print(".------------------------------IN")
            access_new = Access(status='IN', user=user)
            access_new.save()
            return Response(status=status.HTTP_201_CREATED)

        print(".------------------------------OUT")
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

                            #Se ha terminado la semana
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