Role name: bngsudheer.gcsfuse
=========

Add the [gcsfuse yum repository](https://github.com/GoogleCloudPlatform/gcsfuse/blob/master/docs/installing.md).

This role just adds the yum repository. You have to install the packages from this repository yourself. An example is provided.

Requirements
------------

None.

Role Variables
--------------

None.

Dependencies
------------

None.

Example Playbook
----------------

```yml

    - hosts: servers
      roles:
        - bngsudheer.gcsfuse
```

```yml

    - hosts: servers
      tasks:
        - name: install gcsfuse
          yum:
            name: gcsfuse
```

License
-------

BSD


Author Information
------------------

Sudheer Satyanarayana
* Blog: https://www.techchorus.net
* Twitter: https://www.twitter.com/bngsudheer
* Work: https://www.gavika.com
