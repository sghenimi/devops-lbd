# def test_full_address():
#     theater = {
#         "name": "Théâtre des Blancs-Manteaux",
#         "address": "15 Rue des Blancs Manteaux",
#         "post_code": 75004,
#         "city": "Paris",
#         "capacity": 60,
#     }
#     full_address = full_address(theater)
#     assert full_address == "Théâtre des Blancs-Manteaux, 15 Rue des Blancs Manteaux, 75004 Paris"


@pytest.fixture
def theater():
    return {
        "name": "Théâtre des Blancs-Manteaux",
        "address": "15 Rue des Blancs Manteaux",
        "post_code": 75004,
        "city": "Paris",
        "capacity": 60,
    }


def test_full_address(theater):
    full_address = full_address(theater)
    assert full_address == "Théâtre des Blancs-Manteaux, 15 Rue des Blancs Manteaux, 75004 Paris"