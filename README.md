This Permission Management Project follows RBAC model [ROLE BASED ACCESS CONTROL]

Features in the project :
- ROLE :
    User - Can only apply CRUD [create-read-update-delete] their data.
    Staff - Can view all User's data but cannot manipulate the data.
    Admin - Can apply CRUD to all user's data. Admin can also change the role of the user.

- Custom Permission :
  Custom permission "change_role" is used to give the normal user or staff the ability to change the other user's role. This ability can be given only by the user.

- Qr Data:
   User's can get access to their data by the qr image.

API DOCUMENTATION :

![image](https://github.com/Temba23/permission-management-system/assets/126068369/36c5c829-22d1-45cc-9e82-26c2dbd8b8c7)
