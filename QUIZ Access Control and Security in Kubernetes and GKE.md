X A GCP Service account

X A Cloud IAM user account

X A Kubernetes normal user account



O Kubernetes RBAC



X Add your enterprise LDAP or Active Directory domain to Cloud Identity and Access Management.

X Migrate your enterprise user accounts to a Cloud Identity or G Suite organization.

X Deploy an LDAP or Microsoft Active Directory Server for your enterprise as a GCP compute instance.



X A Cloud IAM permission

X A Cloud IAM resource binding

O A Cloud IAM Policy



X A Primitive role

X A Predefined role

X A Project role



X Bind the RBAC role to a Kubernetes service account that has the permissions necessary to manage the objects required by the role.

O Bind the RBAC role to the Kubernetes objects these users need to manage.



O Limit access to some Linux capabilities, for example to grant certain privileges to a process, but not all root user privileges.

Enable AppArmor, which uses security profiles to restrict individual programs actions.