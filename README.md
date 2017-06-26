# rpm-psqlodbc

This repository contains the build files for the psqlodbc package used as a dependency for Immuta software.

## SPEC files

This repository contains two RPM SPEC files. One for builds prior to 1.5.0 which builds with development headers from PostgreSQL 9.5 (psqlodbc95) and one that builds with development headers from PostgreSQL 9.6 (psqlodbc96). The SPEC are configured such that psqlodbc96 conflicts with psqlodbc95, since they lay down the same files, which means you can not have both Postgres versions with Immuta plugins installed at the same time on a single system.

## mock

This repository contains mock files for use in automated builds to ensure that the RPM is being built within a clean chroot. You do not have to use these to manually build the RPM, but this can be used as a guide. More information on Fedora mock here: [https://stg.fedoraproject.org/wiki/Mock?rd=Subprojects/Mock](https://stg.fedoraproject.org/wiki/Mock?rd=Subprojects/Mock)

## jenkins

Jenkins is currently configured to build this RPM and promote manually as necessary under the rpm_psqlodbc job.

### Current issues

If we move to a version above 09.05.0300, we will need to make a small change to our connection strings, update the driver INI, and potentially need a migration script to decrypt existing connections and append the new parameter.
