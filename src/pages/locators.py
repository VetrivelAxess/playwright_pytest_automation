from selenium import webdriver

from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\chromedriver_win32")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.mercadolibre.com/")

from selenium.webdriver.common.by import By


class MercadoLibre:
    click_argentina = "(//a[@class='ml-site-link'])[1]"
    click_bolovia = "(//a[@class='ml-site-link'])[2]"
    click_brazil = "(//a[@class='ml-site-link'])[3]"
    click_chile = "(//a[@class='ml-site-link'])[4]"
    click_colombia = "(//a[@class='ml-site-link'])[5]"
    click_costa = "(//a[@class='ml-site-link'])[6]"
    click_dominic = "(//a[@class='ml-site-link'])[7]"
    click_ecuador = "(//a[@class='ml-site-link'])[8]"
    click_guatemala = "(//a[@class='ml-site-link'])[9]"
    click_hondurus = "(//a[@class='ml-site-link'])[10]"
    click_mexico = "(//a[@class='ml-site-link'])[11]"
    click_nicaragua = "(//a[@class='ml-site-link'])[12]"
    click_panama = "(//a[@class='ml-site-link'])[13]"
    click_paraguay = "(//a[@class='ml-site-link'])[14]"
    click_peru = "(//a[@class='ml-site-link'])[15]"
    click_el_salvador = "(//a[@class='ml-site-link'])[16]"
    click_uruguay = "(//a[@class='ml-site-link'])[17]"
    click_venezuela = "(//a[@class='ml-site-link'])[18]"


class HomePageSelector:
    search_bar = "//input[@class='nav-search-input']"
    search_button = "//div[@class='nav-icon-search']"
    click_ofertas = "//a[text()='Ofertas']"
    click_historial = "//a[text()='Historial']"
    click_supermercado = "(//a[.='Supermercado'])[2]"
    vender_nav_tab = "(//a[.='Vender'])[1]"
    ayuda_nav_tab = "(//a[.='Ayuda'])[1]"
    create_acc = "//a[.='Creá tu cuenta']"
    click_ingresa = "(//a[.='Ingresá'])[1]"
    my_shopping_list = "//a[.='Mis compras']"
    cart_button = "//i[@class='nav-icon-cart']"
    categories_link = "//a[.='Categorías']"


class CategoriesListOptions:
    vehicles_button = "//a[.='Vehículos']"
    estate_button = "//a[.='Inmuebles']"
    supermarket_button = "(//a[.='Supermercado'])[1]"
    technology_button = "//a[.='Tecnología']"
    furniture_button = "//a[.='Hogar y Muebles']"
    home_appliance_button = "//a[.='Electrodomésticos']"
    tools_button = "//a[.='Herramientas']"
    construction_button = "//a[.='Construcción']"
    sports_fitness_button = "//a[.='Deportes y Fitness']"
    vehicle_accessories_button = "//a[.='Accesorios para Vehículos']"
    fashion_button = "//a[.='Moda']"
    games_button = "//a[.='Juegos y Juguetes']"
    drinks_button = "//a[.='Bebés']"
    personal_care_button = "//a[.='Belleza y Cuidado Personal']"
    medical_equip_button = "//a[.='Salud y Equipamiento Médico']"
    industry_offices_button = "//a[.='Industrias y Oficinas']"
    agro_button = "//a[.='Agro']"
    sustainable_product_button = "//a[.='Productos Sustentables']"
    services_button = "//a[.='Servicios']"
    bestseller_button = "//a[.='Más vendidos']"
    official_stores_button = "//a[.='Tiendas oficiales']"
    more_categories_button = "//a[.='Ver más categorías']"


class TechnlogyCategories:
    cell_telephone_button = "//a[.='Celulares y Teléfonos']"
    smartphone_button = "//a[.='Celulares y Smartphones']"
    cell_accessories_button = "//a[.='Accesorios para Celulares']"
    computing_btn = "//a[.='Computación']"
    pc_components_btn = "//a[.='Componentes de PC']"
    print_btn = "//a[.='Impresión']"
    tablet_accessories_btn = "//a[.='Tablets y Accesorios']"
    pc_btn = "//a[.='PC']"
    camera_n_accessories_btn = "//a[.='Cámaras y Accesorios']"
    digital_camera_btn = "//a[.='Cámaras Digitales']"
    camera_accessories_btn = "//a[.='Accesorios para Cámaras']"