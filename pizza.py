class PizzaBase:
    """
    Основа для пиццы из томатного соуса, моцареллы и внутренней логики
    """
    def __init__(self, size: str = 'L'):
        """
        Инициализация экземпляра, задается имя, размер и ингридиенты
        """
        self.name = 'Основа'
        self.size = size
        self.add_ingredients(
            ['томатный соус', 'моцарелла'],
            ['🥫', '🧀']
        )

    def add_ingredients(self, keys: list[str], emojis: list[str]):
        """
        Добавляет массив элементов в словарь с рецептом.
        Если его нет, также создает словарь.
        """
        if not hasattr(self, '_recipe'):
            self._recipe = dict()

        for key, emoji in zip(keys, emojis):
            self._recipe[key] = emoji

    def dict(self):
        """
        Возвращает рецепт пиццы в виде словаря.
        """
        return self._recipe

    def fancy_print(self):
        """
        Вывод рецепта с названием пиццы и эмодзи.
        """
        print(f'{self.name}:', end=' ')
        for key in self.dict().keys():
            print(f'{key}{self.dict()[key]}', end=' ')
        print()

    def __eq__(self, other):
        """
        Сравнение двух пицц.
        Выводит отличия и общие ингредиенты двух пицц.
        Возвращает True при полном совпадении ингредиентов, иначе False.
        """
        similar = dict()
        unique_self = dict()
        unique_other = dict()

        for key in self.dict().keys():
            if key in other.dict().keys():
                similar[key] = self.dict()[key]
            else:
                unique_self[key] = self.dict()[key]

        for key in other.dict().keys():
            if key not in self.dict().keys():
                unique_other[key] = other.dict()[key]

        print('Схожие ингредиенты:', *similar.values())
        print(f'{self.name} уникальные:', *unique_self.values())
        print(f'{other.name} уникальные:', *unique_other.values())

        return self.dict() == other.dict()


class Margherita(PizzaBase):
    """
    Класс пиццы Маргарита с добавлением помидоров.
    Для информации о внутренней логике и прочих ингредиентах см. PizzaBase.
    """
    def __init__(self, size: str = 'L'):
        """
        Инициализация экземпляра, задается имя, размер и ингредиенты.
        """
        super().__init__(size)
        self.name = 'Маргарита'
        self.add_ingredients(
            ['помидоры'],
            ['🍅']
        )


class Pepperoni(PizzaBase):
    """
    Класс пиццы Пепперони с добавлением колбаски пепперони.
    Для информации о внутренней логике и прочих ингредиентах см. PizzaBase.
    """
    def __init__(self, size: str = 'L'):
        """
        Инициализация экземпляра, задается имя, размер и ингредиенты.
        """
        super().__init__(size)
        self.name = 'Пепперони'
        self.add_ingredients(
            ['пепперони'],
            ['🔴']
        )


class Hawaiian(PizzaBase):
    """
    Класс гавайской пиццы с добавлением курицы и ананасов.
    Для информации о внутренней логике и прочих ингредиентах см. PizzaBase.
    """
    def __init__(self, size: str = 'L'):
        """
        Инициализация экземпляра, задается имя, размер и ингредиенты.
        """
        super().__init__(size)
        self.name = 'Гавайская'
        self.add_ingredients(
            ['курица', 'ананасы'],
            ['🐔', '🍍']
        )
