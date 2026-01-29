# Managing Permissions and Groups in Django

## Custom Permissions
The Book model in the bookshelf app defines the following permissions:
- can_view
- can_create
- can_edit
- can_delete

## Groups
The following groups were created using the Django admin panel:
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: all permissions

## Permission Enforcement
Views are protected using Django's @permission_required decorator
with raise_exception=True to enforce access control.

## Testing
Users were assigned to different groups and tested by attempting
to access protected views to verify permission enforcement.
