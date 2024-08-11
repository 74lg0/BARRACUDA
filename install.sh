#!/bin/bash

# Required packages
required_packages=(
    "python3"
    "tor"
)

required_pip_packages=(
    "threading"
    "pystyle"
    "pysocks"
)

check_installation() {
    which $1 > /dev/null 2>&1
}

install_package() {
    echo -e "\e[32m[!] Instalando $1\e[0m"
    if [ "$(uname)" == "Darwin" ]; then
        brew install $1
    elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
        sudo apt-get install $1
    fi
}

install_pip_package() {
    echo -e "\e[32m[!] Instalando $1\e[0m"
    pip install $1
}

main() {
    all_installed=true
    for package in "${required_packages[@]}"; do
        if ! check_installation $package; then
            all_installed=false
            install_package $package
        fi
    done

    for package in "${required_pip_packages[@]}"; do
        if ! python3 -c "import $package" > /dev/null 2>&1; then
            all_installed=false
            install_pip_package $package
        fi
    done

    if $all_installed; then
        echo "Todos los requerimientos ya están instalados"
        echo -e "Inicia una instancia de tor en otra pestaña de terminal con el comando: tor"
    fi
}

main
