#!/bin/bash

rpmlint /rpmbuild/SPECS/*.spec
for spec_file in /rpmbuild/SPECS/*.spec; do
    rpmbuild -D "dist .el6" -D "version ${version}" -D "_topdir /rpmbuild" -ba ${spec_file}
done
