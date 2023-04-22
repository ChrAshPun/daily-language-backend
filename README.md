# IT Blog

04/2023 - I need to create ITBlog models and serializers that will be used by the ITBlog (React) website
1. Create a Django app: Run the startapp command to create a new Django app. For example, python manage.py startapp myapp.
2. Add app to INSTALLED_APPS: In the settings.py file of your project, add your app to the INSTALLED_APPS list.
3. Create the model: In the models.py file of your app, define your model using Django's ORM. (Need one-to-many relationship this time, Sqlite does not support ArrayField)
4. makemigrations and migrate - creates a set of instructions that Django can use to modify the database schema to match the new model definitions
5. Add model to admin panel: In the admin.py file of your app, register your model with the admin site.
6. Add serializer: In the serializers.py file of your app, create a serializer class that defines how your model should be serialized and deserialized.
7. Create the view: In the views.py file of your app, create a view function that handles HTTP requests and returns a response.
8. Add view to urls.py: In the urls.py file of your app, add a URL pattern that maps a URL to your view function.