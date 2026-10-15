# Ouvert à l’extension, fermé à la modification :
# Une classe doit pouvoir être étendue sans avoir à la modifier.

from abc import ABC, abstractmethod
from typing import Mapping


class Widget():
    def get_dashboard_widget_data(self, id: str) -> Mapping:
        ...

    def get_pdf_widget_data(self, id: str) -> Mapping:
        ...

#Good
class Widget(ABC):

    @abstractmethod
    def get_data(self, id: str) -> Mapping:
        ...

# Si on veut un widget différent, mieux vaut créer une hiérarchie :
# Ainsi, on étend le comportement sans toucher à la classe de base.
class WidgetDashBoard(Widget):
    def get_data(self, id: str) -> Mapping:
        ...


class PDFWidget(Widget):
    def get_data(self, id: str) -> Mapping:
        ...