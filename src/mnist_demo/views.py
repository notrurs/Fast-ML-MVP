from base64 import b64encode, b64decode
import json
from io import BytesIO

from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from django.http import JsonResponse

from .forms import UploadImageForm
from .mixins import UserContextMixin
from .services import model


class IndexPage(TemplateView):
    template_name = 'mnist_demo/index.html'


class FormUpload(UserContextMixin, FormView):
    template_name = 'mnist_demo/form_upload_page.html'
    form_class = UploadImageForm

    def form_valid(self, form):
        if form.is_valid():
            context = self.get_context_data()

            # Write prediction
            uploaded_file = self.request.FILES['image'].file
            context['prediction'] = model.predict(uploaded_file)

            # Write uploaded image
            encoded_image = b64encode(uploaded_file.getvalue()).decode()
            context['image'] = f"data:image/jpeg;base64,{encoded_image}"

            # Write predicted num with max prob
            context['predicted_num'] = max(context['prediction'], key=context['prediction'].get)

            return render(self.request, FormUpload.template_name, context)
        else:
            return redirect('mnist_demo:form_upload')


class AjaxDraw(UserContextMixin, TemplateView):
    template_name = 'mnist_demo/ajax_drawing_page.html'

    def post(self, request, *args, **kwargs):
        image = json.loads(request.body.decode())['image']
        prediction = model.predict(BytesIO(b64decode(image)))
        response = {
            'data': {
                'prediction': prediction,
                'predicted_num': max(prediction, key=prediction.get)
            }
        }
        return JsonResponse(response)


class WsDraw(UserContextMixin, TemplateView):
    template_name = 'mnist_demo/ws_drawing_page.html'
