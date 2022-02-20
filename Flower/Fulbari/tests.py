from django.test import Client, SimpleTestCase , TestCase
from django.urls import reverse, resolve
from Fulbari.views import home, product, about, blog_detail, dashboard
from Product.views import admin_add_product_view, admin_products_view
from django.contrib.auth.models import User, auth 
from Product.models import Product



class TestUrls(SimpleTestCase):
    def test_resolve_to_home(self):
        url = reverse("home")
        resolver = resolve(url)
        self.assertEquals(resolver.func,home)


    def test_resolve_to_about(self):
        url = reverse("about")
        resolver = resolve(url)
        self.assertEquals(resolver.func,about)


    def test_resolve_to_product(self):
        url = reverse("product")
        resolver = resolve(url)
        self.assertEquals(resolver.func,product)

    
    def test_resolve_to_dashboard(self):
        url = reverse("dashboard")
        resolver = resolve(url)
        self.assertEquals(resolver.func,dashboard)    


class TestView(TestCase):
    def test_register_view(self):
        client = Client()
        response = client.get(reverse("register"))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'pages/register.html')


    def test_add_product_view(self):  
        client = Client()
        logged_in = client.login(username = 'admin',password ='admin')
        response = client.get(reverse("admin_products_view"))
        self.assertEquals(response.status_code,302)
        self.assertTemplateUsed(response,'adminControl/admin_product.html')        
       


