FROM centos:6.6

ENV version="09.05.0300"

RUN yum -y install \
        https://download.postgresql.org/pub/repos/yum/9.5/redhat/rhel-6-x86_64/pgdg-centos95-9.5-3.noarch.rpm \
        https://download.postgresql.org/pub/repos/yum/9.6/redhat/rhel-6-x86_64/pgdg-centos96-9.6-3.noarch.rpm \
        && \
    rpm --rebuilddb && \
    yum install -y \
        automake \
        libtool \
        make \
        postgresql95-devel \
        postgresql96-devel \
        rpm-build \
        rpmlint \
        tar\
        unixODBC-devel \
        && \
    mkdir -p /rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS} && \
    useradd builder -u 1000 -m -G users,wheel

ADD  https://ftp.postgresql.org/pub/odbc/versions/src/psqlodbc-${version}.tar.gz /rpmbuild/SOURCES/
COPY SPECS/*.spec /rpmbuild/SPECS/
RUN chown -R builder. /rpmbuild

COPY pkg/el6/build_rpms.sh /tmp/build_rpms.sh

USER builder
CMD ["/tmp/build_rpms.sh"]
