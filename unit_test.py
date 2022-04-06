# =======
# IMPORTS
# =======

import unittest
import flask
import json
import os
import pickle


# =======
# EXEMPLE TEST UNITAIRE
# =======

with app.test_client() as c:
    response = c.get('/multi-upload')
    self.assertEquals(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
