import os
import django
from datetime import datetime, date

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "logisticsDeliveryPlanner.settings")
django.setup()

from drivers.models import Driver
from vehicles.models import Vehicle
from routes.models import DeliveryPoint, Route, Assignment
from vehicles.choices import VehicleTypeChoices


def populate_db():
    #Drivers
    driver1=Driver.objects.create(
        full_name="Milen Nikolov",
        date_of_birth=date(1987, 7, 30),
        phone_number="0888123456",
        driving_license_number="AB123CD456",
        years_of_experience=15,
        is_active=True
    )
    driver2=Driver.objects.create(
        full_name="Petar Ivanov",
        date_of_birth=date(1968, 7, 21),
        phone_number="0888234567",
        driving_license_number="ZX987YT654",
        years_of_experience=32,
        is_active=True
    )
    driver3=Driver.objects.create(
        full_name="Ivan Georgiev",
        date_of_birth=date(1990, 11, 2),
        phone_number="0888345678",
        driving_license_number="PL456MN789",
        years_of_experience=8,
        is_active=True
    )
    driver4=Driver.objects.create(
        full_name="Bozhidar Nikolov",
        date_of_birth=date(1982, 5, 17),
        phone_number="0888456789",
        driving_license_number="QW123ER456",
        years_of_experience=18,
        is_active=True
    )
    driver5=Driver.objects.create(
        full_name="Marian Iliev",
        date_of_birth=date(1995, 9, 30),
        phone_number="0888567890",
        driving_license_number="RT789YU123",
        years_of_experience=5,
        is_active=False
    )
    driver6=Driver.objects.create(
        full_name="Kristian Ivanov",
        date_of_birth=date(1985, 1, 8),
        phone_number="0888678901",
        driving_license_number="GH456JK789",
        years_of_experience=12,
        is_active=True
    )
    driver7=Driver.objects.create(
        full_name="Ilia Peichev",
        date_of_birth=date(1975, 6, 25),
        phone_number="0888789012",
        driving_license_number="VB789NM456",
        years_of_experience=25,
        is_active=False
    )
    driver8=Driver.objects.create(
        full_name="Tihomir Petkov",
        date_of_birth=date(1989, 4, 19),
        phone_number="0888890123",
        driving_license_number="AS234DF567",
        years_of_experience=10,
        is_active=True
    )
    driver9=Driver.objects.create(
        full_name="Dimitar Kostov",
        date_of_birth=date(1992, 12, 5),
        phone_number="0888901234",
        driving_license_number="KL567OP890",
        years_of_experience=7,
        is_active=True
    )
    driver10=Driver.objects.create(
        full_name="Todor Peev",
        date_of_birth=date(1980, 8, 14),
        phone_number="0888012345",
        driving_license_number="ZX345CV678",
        years_of_experience=20,
        is_active=True
    )


    #Vehicles
    vehicle1=Vehicle.objects.create(
        registration_number="CA1234AB",
        make="Ford",
        model="Transit",
        vehicle_type=VehicleTypeChoices.VAN,
        capacity_kg=3500,
        manufacture_date=date(2018, 5, 10)
    )
    vehicle2=Vehicle.objects.create(
        registration_number="CB5678PA",
        make="Mercedes",
        model="Sprinter",
        vehicle_type=VehicleTypeChoices.VAN,
        capacity_kg=5000,
        manufacture_date=date(2020, 3, 15)
    )
    vehicle3=Vehicle.objects.create(
        registration_number="CC9012E",
        make="Volvo",
        model="FH",
        vehicle_type=VehicleTypeChoices.TRUCK,
        capacity_kg=18000,
        manufacture_date=date(2019, 7, 20)
    )
    vehicle4=Vehicle.objects.create(
        registration_number="BT3456H",
        make="MAN",
        model="TGL",
        vehicle_type=VehicleTypeChoices.TRUCK,
        capacity_kg=12000,
        manufacture_date=date(2017, 9, 12)
    )
    vehicle5=Vehicle.objects.create(
        registration_number="A7890CC",
        make="Iveco",
        model="Daily",
        vehicle_type=VehicleTypeChoices.VAN,
        capacity_kg=3200,
        manufacture_date=date(2021, 1, 5)
    )
    vehicle6=Vehicle.objects.create(
        registration_number="B1122KA",
        make="Renault",
        model="Master",
        vehicle_type=VehicleTypeChoices.VAN,
        capacity_kg=3500,
        manufacture_date=date(2016, 11, 18)
    )
    vehicle7=Vehicle.objects.create(
        registration_number="PB3344MH",
        make="Scania",
        model="R450",
        vehicle_type=VehicleTypeChoices.TRUCK,
        capacity_kg=20000,
        manufacture_date=date(2018, 6, 30)
    )
    vehicle8=Vehicle.objects.create(
        registration_number="CB5566OP",
        make="DAF",
        model="XF",
        vehicle_type=VehicleTypeChoices.TRUCK,
        capacity_kg=19000,
        manufacture_date=date(2019, 2, 22)
    )
    vehicle9=Vehicle.objects.create(
        registration_number="CA7788A",
        make="Volkswagen",
        model="Crafter",
        vehicle_type=VehicleTypeChoices.VAN,
        capacity_kg=3000,
        manufacture_date=date(2022, 4, 14)
    )
    vehicle10=Vehicle.objects.create(
        registration_number="CH9900CT",
        make="Skoda",
        model="Octavia",
        vehicle_type=VehicleTypeChoices.CAR,
        capacity_kg=300,
        manufacture_date=date(2024, 8, 9)
    )


    #Delivery Points
    delivery_point1=DeliveryPoint.objects.create(
        address="Simeonovsko Shose 110",
        city="Sofia",
        description="Fantastico Store"
    )
    delivery_point2=DeliveryPoint.objects.create(
        address="Nezavisimost 42",
        city="Plovdiv",
        description="Econt Distribution center"
    )
    delivery_point3=DeliveryPoint.objects.create(
        address="Hristo Botev 21",
        city="Varna",
        description="Billa Central Warehouse"
    )
    delivery_point4=DeliveryPoint.objects.create(
        address="Tsar Boris III 11",
        city="Sofia"
    )
    delivery_point5=DeliveryPoint.objects.create(
        address="Bulgaria 82",
        city="Ruse",
        description="Speedy Distribution center"
    )
    delivery_point6=DeliveryPoint.objects.create(
        address="Ivan Vazov 16",
        city="Stara Zagora",
        description="Warehouse"
    )
    delivery_point7=DeliveryPoint.objects.create(
        address="Panorama 22",
        city="Pleven"
    )
    delivery_point8=DeliveryPoint.objects.create(
        address="Industiralna 42",
        city="Shumen",
        description="Local Store"
    )
    delivery_point9=DeliveryPoint.objects.create(
        address="Cherno More 4",
        city="Burgas"
    )
    delivery_point10=DeliveryPoint.objects.create(
        address="Tsvetan Lazarov 55",
        city="Sofia",
        description="Kaufland Store"
    )

    #Routes
    route1=Route.objects.create(
        name="Sofia - Plovdiv",
        start_location="Sofia",
        end_location="Plovdiv",
        distance_km=145,
        estimated_duration_minute=120
    )
    route2=Route.objects.create(
        name="Sofia - Varna",
        start_location="Sofia",
        end_location="Varna",
        distance_km=470,
        estimated_duration_minute=420
    )
    route3=Route.objects.create(
        name="Plovdiv - Burgas",
        start_location="Plovdiv",
        end_location="Burgas",
        distance_km=250,
        estimated_duration_minute=240
    )
    route4=Route.objects.create(
        name="Varna - Ruse",
        start_location="Varna",
        end_location="Ruse",
        distance_km=200,
        estimated_duration_minute=210
    )
    route5=Route.objects.create(
        name="Burgas - Stara Zagora",
        start_location="Burgas",
        end_location="Stara Zagora",
        distance_km=180,
        estimated_duration_minute=190
    )
    route6=Route.objects.create(
        name="Ruse - Pleven",
        start_location="Ruse",
        end_location="Pleven",
        distance_km=140,
        estimated_duration_minute=150
    )
    route7=Route.objects.create(
        name="Pleven - Sofia",
        start_location="Pleven",
        end_location="Sofia",
        distance_km=170,
        estimated_duration_minute=160
    )
    route8=Route.objects.create(
        name="Sofia - Haskovo",
        start_location="Sofia",
        end_location="Haskovo",
        distance_km=230,
        estimated_duration_minute=210
    )
    route9=Route.objects.create(
        name="Varna - Burgas",
        start_location="Varna",
        end_location="Burgas",
        distance_km=108,
        estimated_duration_minute=80
    )
    route10=Route.objects.create(
        name="Plovdiv - Shumen",
        start_location="Plovdiv",
        end_location="Shumen",
        distance_km=320,
        estimated_duration_minute=300
    )


    #Assign delivery points to routes
    route1.points_for_delivery.add(delivery_point1, delivery_point8, delivery_point10)
    route2.points_for_delivery.add(delivery_point4, delivery_point7)
    route3.points_for_delivery.add(delivery_point5, delivery_point6, delivery_point8, delivery_point9)
    route4.points_for_delivery.add(delivery_point2, delivery_point10)
    route5.points_for_delivery.add(delivery_point8)
    route6.points_for_delivery.add(delivery_point5, delivery_point6)
    route7.points_for_delivery.add(delivery_point4, delivery_point5, delivery_point8)
    route8.points_for_delivery.add(delivery_point1, delivery_point2, delivery_point5, delivery_point9)
    route9.points_for_delivery.add(delivery_point2, delivery_point4, delivery_point7, delivery_point8, delivery_point10)
    route10.points_for_delivery.add(delivery_point6, delivery_point7)


    #Assignments
    assignment=Assignment.objects.create(
        route=route1,
        driver=driver1,
        vehicle=vehicle1,
        assignment_start=datetime(2026, 5, 1, 8, 0),
        notes="Morning delivery"
    )
    assignment=Assignment.objects.create(
        route=route2,
        driver=driver1,
        vehicle=vehicle2,
        assignment_start=datetime(2026, 5, 2, 6, 30),
        notes="Fragile Stock"
    )
    assignment3=Assignment.objects.create(
        route=route5,
        driver=driver10,
        vehicle=vehicle8,
        assignment_start=datetime(2026, 5, 3, 9, 0),
        notes="Chilled Products"
    )
    assignment4=Assignment.objects.create(
        route=route4,
        driver=driver8,
        vehicle=vehicle2,
        assignment_start=datetime(2026, 5, 3, 7, 45)
    )
    assignment5=Assignment.objects.create(
        route=route7,
        driver=driver9,
        vehicle=vehicle2,
        assignment_start=datetime(2026, 5, 5, 10, 15),
        notes="Fresh Produce"
    )
    assignment6=Assignment.objects.create(
        route=route1,
        driver=driver1,
        vehicle=vehicle6,
        assignment_start=datetime(2026, 5, 6, 8, 30),
        notes="Standard Cargo"
    )
    assignment7=Assignment.objects.create(
        route=route3,
        driver=driver6,
        vehicle=vehicle3,
        assignment_start=datetime(2026, 5, 6, 5, 45),
        notes="Heavy cargo"
    )
    assignment8=Assignment.objects.create(
        route=route5,
        driver=driver9,
        vehicle=vehicle9,
        assignment_start=datetime(2026, 5, 6, 11, 0)
    )
    assignment9=Assignment.objects.create(
        route=route5,
        driver=driver4,
        vehicle=vehicle4,
        assignment_start=datetime(2026, 5, 9, 9, 20),
        notes="Frozen Products"
    )
    assignment10=Assignment.objects.create(
        route=route5,
        driver=driver10,
        vehicle=vehicle10,
        assignment_start=datetime(2026, 5, 10, 6, 0),
        notes="Hazardous Materials"
    )

# populate_db()


