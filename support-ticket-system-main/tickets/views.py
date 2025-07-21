from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions

from .models import Ticket
from .serializers import TicketSerializer
from .permissions import IsOwnerOrAdmin, IsAdmin

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def get_queryset(self):
        user = self.request.user
        return Ticket.objects.all() if user.is_staff else Ticket.objects.filter(created_by=user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_permissions(self):
        if self.action == 'status':
            return [IsAdmin()]
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [IsOwnerOrAdmin()]
        return [permissions.IsAuthenticated()]

    @action(detail=True, methods=['patch'], url_path='status', permission_classes=[IsAdmin])
    def status(self, request, pk=None):
        ticket = self.get_object()
        status_value = request.data.get("status")
        if status_value not in dict(Ticket.STATUS_CHOICES).keys():
            return Response({"error": "Invalid status"}, status=400)
        ticket.status = status_value
        ticket.save()
        return Response(TicketSerializer(ticket).data)
