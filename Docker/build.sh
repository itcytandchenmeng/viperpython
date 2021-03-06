#!/usr/bin/env bash
cd /root/viper/
mv ./Docker/CONFIG_docker.py CONFIG.py
chmod 755 viper.py
find . -type f -exec dos2unix {} \;

# clean viper
rm -rf /root/viper/*.lock
rm -rf /root/viper/*.pid
rm -rf /root/viper/*.sock
chmod 777 -R /root/viper/Docker/db/
rm -rf /root/viper/Docker/db/*
rm -rf /root/viper/Docker/log/*
rm -rf /root/viper/Docker/module/*
rm -rf /root/.msf4/logs/*

# clean install cache
rm -rf /root/.cache/*
rm -rf /root/.bundle/cache
rm -rf /root/.gem/specs
rm -rf /usr/local/lib/ruby/gems/2.6.0/doc/*
rm -rf /usr/local/lib/ruby/gems/2.6.0/cache/*
rm -rf /usr/local/share/ri/2.6.0/system
rm -rf /usr/lib/python3

# clean metasploit-framework
rm -rf /root/metasploit-framework/external/*
rm -rf /root/metasploit-framework/documentation/*
rm -rf /root/metasploit-framework/spec/*
rm -rf /root/metasploit-framework/docker/*
rm -rf /root/metasploit-framework/test/*

# clean gem
gem cleanup