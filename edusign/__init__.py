__version__ = "0.0.3"
__author__ = "jules.lasne@gmail.com"


from edusign.models import Students
from edusign.models import Professors
from edusign.models import Groups
from edusign.models import Courses
from edusign.utils import EdusignAPIError

__all__ = ["Students", "Professors", "Groups", "Courses", "EdusignAPIError"]
