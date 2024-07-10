from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """
    Allow users to edit their own profiles
    """

    # obj is the model instance for which permissions are being checked 
    def has_object_permission(self, request, view, obj):
        """ 
        Check user trying to edit a user profile and only allow if user is trying to update their own profile 
        """

        if request.method == permissions.SAFE_METHODS:
            return True 

        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """ 
    Allow user to update their own status
    """

    def has_object_permission(self, request, view, obj):
        """ 
        Check user has permission to update a status
        """
        if request.method in permissions.SAFE_METHODS:
            return True 

        # if a user is updating a status, it has to be the user's own feed 
        return obj.user_profile.id == request.user.id




