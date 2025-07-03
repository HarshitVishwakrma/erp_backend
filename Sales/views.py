from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from .models import onwardchallan
from .models import transportdetails
from .models import vehicaldetails
from .models import outwardchallan
from .serializers import OnwardChallanSerializer
from .serializers import transportdetailsSerializer
from .serializers import vehicaldetailsSerializer
from .serializers import outwardchallanSerializer
from .utils import create_challanNumber
from All_Masters.models import Item as Item2
from All_Masters.serializers import ItemSerializer
from Purchase.models import PurchasePO 
class OnwardChallanViewSet(viewsets.ModelViewSet):
    queryset = onwardchallan.objects.all()
    serializer_class = OnwardChallanSerializer
class transportdetailsview(viewsets.ModelViewSet):
    queryset=transportdetails.objects.all()
    serializer_class=transportdetailsSerializer

class vehicaldetailsview(viewsets.ModelViewSet):
    queryset=vehicaldetails.objects.all()
    serializer_class=vehicaldetailsSerializer
class outwardchallanview(viewsets.ModelViewSet):
    queryset=outwardchallan.objects.all()
    serializer_class=outwardchallanSerializer
    
class deletechallan(APIView):
    def delete(self, request,id):
        # challan_no = request.data.get('challan_no')
        # if not challan_no:
        #     return Response({'error': 'challan_no is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            challan = onwardchallan.objects.get(challan_no=id)
            challan.delete()
            return Response({'message': f'Challan {id} deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except onwardchallan.DoesNotExist:
            return Response({'error': 'Challan not found'}, status=status.HTTP_404_NOT_FOUND)


class generate_unique_challan_number(APIView):
    def get(self, request):
        try:
            challan_no = create_challanNumber()
            return Response({"Challan_no" : challan_no}, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class deletetransportdetails(APIView):
    def delete(self,request,name):
        try:
            transport_name=transportdetails.objects.get(transport_name=name)
            transport_name.delete()
            return Response({'message': f'transport_name {name} deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except transportdetails.DoesNotExist:
            return Response({'error': 'transport_name not found'}, status=status.HTTP_404_NOT_FOUND)


        
class edittransportdetails(APIView):
    def put(self, request, name):
        try:
            # Find the transportdetails by transport_name
            transport_obj = transportdetails.objects.get(transport_name=name)
        except transportdetails.DoesNotExist:
            return Response({'error': 'transport_name not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # Get new EWAY_bill_no from request body
        new_eway_bill_no = request.data.get('EWAY_bill_no')
        if not new_eway_bill_no:
            return Response({'error': 'EWAY_bill_no is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Update
        transport_obj.EWAY_bill_no = new_eway_bill_no
        transport_obj.save()

        return Response({
            'message': f'transport_name {name} updated successfully',
            'transport_name': transport_obj.transport_name,
            'EWAY_bill_no': transport_obj.EWAY_bill_no,
            'serial_no': transport_obj.serial_no,
        }, status=status.HTTP_200_OK)

class editvehicaldetails(APIView):
    def put(self, request, vehical_no):
        try:
            vehicle = vehicaldetails.objects.get(vehical_no=vehical_no)
        except vehicaldetails.DoesNotExist:
            return Response({'error': 'Vehicle not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = vehicaldetailsSerializer(vehicle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class deletevehicaldetails(APIView):
    def delete(self,request,name):
        try:
            vehical_no=vehicaldetails.objects.get(vehical_no=name)
            vehical_no.delete()
            return Response({'message':f'vehical_no {name} deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except transportdetails.DoesNotExist:
            return Response({'error':'vehical_no not found'}, status=status.HTTP_404_NOT_FOUND)


class purchaseview(APIView):
    def post(self, request):
        
        purchase_order = request.data.get('purchase_order')
        item_code = request.data.get('item_code')
        description = request.data.get('description')
        quantity = request.data.get('quantity')
        unit_price = request.data.get('unit_price')
        total_price = request.data.get('total_price')

    
        if not purchase_order or not item_code:
            return Response(
                {"error": "purchase_order and item_code are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        queryset = Item2.objects.all()
        queryset = queryset.filter(purchase_order=purchase_order, item_code=item_code)

        if description:
            queryset = queryset.filter(description__icontains=description)
        if quantity:
            queryset = queryset.filter(quantity=quantity)
        if unit_price:
            queryset = queryset.filter(unit_price=unit_price)
        if total_price:
            queryset = queryset.filter(total_price=total_price)

        serializer = ItemSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class challanview(APIView):
    def get(self, request):
        challan_no = request.query_params.get('challan_no')
        if not challan_no:
            return Response({"error": "challan_no parameter is required."}, status=400)

        try:
            challan = onwardchallan.objects.get(challan_no=challan_no)
        except onwardchallan.DoesNotExist:
            return Response({"error": "Challan not found."}, status=404)

        serializer = OnwardChallanSerializer(challan)
        return Response(serializer.data)
    
class inwardchallanview(APIView):
    def get(self, request):
        supplier = request.query_params.get('supplier')
        if not supplier:
            return Response({"error": "supplier parameter is required."}, status=400)

        #  Find all PurchasePOs for this supplier
        purchase_orders = PurchasePO.objects.filter(Supplier__iexact=supplier)
        if not purchase_orders.exists():
            return Response({"error": f"No PurchasePO found for supplier '{supplier}'"}, status=404)

        results = []
        for po in purchase_orders:
            items = Item2.objects.filter(purchase_order=po)
            items_data = ItemSerializer(items, many=True).data

            results.append({
                "purchase_order_no": po.PoNo,
                "items": items_data
            })

        return Response({
            "supplier": supplier,
            "results": results
        }, status=status.HTTP_200_OK)
