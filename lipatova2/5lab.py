from owlready2 import *

# Загрузка онтологии
onto = get_ontology("internet_protocols.owl").load()

# Функция для создания нового класса
def create_new_class():
    class_name = input("Введите имя нового класса: ")
    parent_class_name = input("Введите имя родительского класса: ")
    
    parent_class = onto.search_one(iri=f"*{parent_class_name}*")
    if parent_class:
        with onto:
            new_class = types.new_class(class_name, (parent_class,))
        print(f"Создан новый класс {class_name} как подкласс {parent_class_name}")
    else:
        print("Родительский класс не найден")

# Функция для поиска
def search_in_ontology():
    search_term = input("Введите термин для поиска: ")
    results = onto.search(iri=f"*{search_term}*")
    
    if results:
        print("Результаты поиска:")
        for item in results:
            print(item.name)
    else:
        print("Ничего не найдено")

# Функция для выполнения запросов
def run_queries():
    print("\nВыполнение запросов:")
    
    # Запрос 1: Найти все протоколы транспортного уровня
    transport_protocols = list(onto.TransportLayerProtocol.subclasses())
    print("\n1. Протоколы транспортного уровня:")
    for p in transport_protocols:
        print(p.name)
    
    # Запрос 2: Найти протоколы с портом 80
    print("\n2. Протоколы, использующие порт 80:")
    for p in onto.Protocol.instances():
        if hasattr(p, "hasPortNumber") and p.hasPortNumber == 80:
            print(p.name)
    
    # Запрос 3: Найти зашифрованные протоколы
    print("\n3. Зашифрованные протоколы:")
    for p in onto.Protocol.instances():
        if hasattr(p, "requiresEncryption") and p.requiresEncryption:
            print(p.name)

# Главное меню
def main_menu():
    while True:
        print("\nМеню:")
        print("1. Создать новый класс")
        print("2. Выполнить поиск")
        print("3. Выполнить запросы")
        print("4. Сохранить онтологию")
        print("5. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            create_new_class()
        elif choice == "2":
            search_in_ontology()
        elif choice == "3":
            run_queries()
        elif choice == "4":
            onto.save(file = "internet_protocols_updated.owl")
            print("Изменения сохранены")
        elif choice == "5":
            break
        else:
            print("Неверный выбор")

if __name__ == "__main__":
    main_menu()