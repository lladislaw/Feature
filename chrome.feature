Feature: Поиск авто на авито
  Scenario: Выбор параметров поиска

    When Зашли на сайт avito.ru
    Then Выбрали категорию Авто
    And Выбрали марку "Subaru"
    And Выбрали тип коробки передач "Механика"
    And Ввели цену от "100000" до "200000" рублей
    Then Нажали на кнопку поиска
    And Выбрали сортировку "Дешевле"

