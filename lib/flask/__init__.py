# encoding: utf-8

"""
@version: 1.0
@author: dawning
@contact: dawning7670@gmail.com
@time: 2017/4/1 8:59
"""

from app import app
from lib.utils import package_import

package_import("app.views")
package_import("lib.flask.errors")
package_import("lib.flask.intercept")
package_import("app.intercept")
