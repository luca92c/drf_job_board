from django.shortcuts import render
from rest_framework.views import APIView  #class based APIVIew
from jobs.models import JobOffer
from rest_framework.response import Response
from jobs.serializers import JobOfferSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

class JobOfferAPIView(APIView):
    """List all job offers"""

    def get(self, request):
        job_offers = JobOffer.objects.all()
        serializer = JobOfferSerializer(job_offers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JobOfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobOfferDetailAPIView(APIView):
    """List a job offer"""

    def get_object(self, pk):
        return get_object_or_404(JobOffer, pk=pk)

    def get(self, request, pk):
        job_offer = self.get_object(pk)
        serializer = JobOfferSerializer(job_offer)
        return Response(serializer.data)

    def put(self, request, pk):
        job_offer = self.get_object(pk)
        serializer = JobOfferSerializer(job_offer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        job_offer = self.get_object(pk)
        job_offer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)