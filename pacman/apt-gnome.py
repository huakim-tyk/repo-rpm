#!/bin/python3
#use File::Basename;
#use File::Spec;
#require File::Spec->catfile(dirname(__FILE__), 'apt-gui.pl');
#our @pkgs;

#push @pkgs, qw(
#tangram
#valent
#gnomesu
#);
j=__import__('apt-gui')
pkgs=j.pkgs
main=j.main

pkgs.extend((
"adwaita-gtk2-theme",
"alacarte",
"celluloid",
"dconf-editor",
"eog",
"file-roller",
"gcr3",
"gdm",
"gjs",
"gnome-color-manager",
"gnome-control-center",
"gnome-disk-utility",
"gnome-extensions-app",
"gnome-keyring",
"gnome-menus",
"gnome-power-manager",
"gnome-session-wayland-session",
"gnome-session-xsession",
"gnome-shell-extension-appindicator",
"gnome-shell-extension-dash-to-dock",
"gnome-system-monitor",
"gnome-terminal",
"gnome-themes-extra",
"gnome-tweaks",
"gparted",
"gvfs",
"gvfs-fuse",
"gvfs-mtp",
"libnma",
"nautilus",
"pavucontrol",
"file-roller-nautilus",
"gnome-terminal-nautilus",
"polkit-gnome",
"qgnomeplatform-qt5",
"qgnomeplatform-qt6",
"redshift",
"secrets",
"xdg-desktop-portal-gtk"
))

for i in ('good', 'bad-free', 'base', 'ugly-free'):
    pkgs.append("gstreamer1-plugins-"+i)

pkgs.extend((
'epiphany',
'evolution'
))

if __name__ == '__main__': 
    main()
