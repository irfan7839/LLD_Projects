from country import Country
from international_provider import InternationalProvider
from england_factory import EnglandFactory
from spain_factory import SpainFactory


# client Code


def main(country):

    factory = InternationalProvider.create(country)
    language = factory.create_language()
    capital_city = factory.create_capital()
    print(f"Country: {country.name}")
    print(f"Language: {language.__class__.__name__}")
    print(f"Greet: {language.greet()}")
    print(f"Capital: {capital_city.__class__.__name__}")
    print(f"Total Population: {capital_city.get_population()}")
    print(f"Total Attractions: {capital_city.list_top_attraction()}")


if __name__ == "__main__":
    country_name = Country.SPAIN
    main(country_name)
