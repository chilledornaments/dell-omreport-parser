#!/usr/bin/env bash

if [ "${UID}" != 0 ]
then
echo "Please run as root"
exit 1
fi



install_cron () {
    RAND=$(shuf -i 0-59 -n 1)
    echo "$RAND * * * * root /opt/dell-omreport-parser/metric_collector.sh >> /opt/dell-omreport-parser/cron.log 2>&1" > /etc/cron.d/omsa-metrics
    echo "Installed cronjob to /etc/cron.d/omsa-metrics"
    echo ""
    echo "Install finished"
}
schedule () {
    echo ""
    echo "Metrics will be collected every hour"
    read -p "Is this OK? [y/n]" answer
    if [ "${input}"  == "y" ]
    then
    install_cron
    elif [ "${input}"  == "n" ]
    then
    echo ""
    echo "You will need to install the cronjob on your own"
    echo ""
    echo "Check metric_collector.sh for more info"
    exit 2
    fi
}

install_packages () {
    if [ "${PKG_MGR}" == "yum" ]
    then
    rhel_packages=("epel-release" "python36" "python36-devel" "python36-setuptools")
    for package in ${rhel_packages[@]}
    do
    yum -y install "${package}" > /dev/null
    done
    easy_install-3.6 pip 
    pip3 install requests
    schedule
    elif [ "${PKG_MGR}" == "apt" ]
    then
    deb_packages=("I'm an RHCSA")
    for package in ${deb_packages[@]}
    do
    apt -y install "${package}" > /dev/null
    done
    schedule
    fi
    
}

confirm_install() {
    read -p "Proceed with installation? [y/n] " input
    if [ "${input}"  == "y" ]
    then
    install_packages
    elif [ "${input}"  == "n" ]
    then
    exit 2
    fi
}



get_package_manager () {
    if $(which yum > /dev/null 2>&1)
    then
    PKG_MGR=yum
    elif $(which apt > /dev/null 2>&1)
    then
    PKG_MGR=apt
    else
    echo "Unable to detect package manager. Exiting."
    exit 1
    fi
    echo "******************************************************"
    echo "Detected package manager is: ${PKG_MGR}"
    echo "******************************************************"
    confirm_install

}


get_package_manager