subarch: amd64
version_stamp: latest
target: livecd-stage1
rel_type: default
profile: default/linux/amd64/17.0/no-multilib
snapshot: latest
source_subpath: default/stage3-amd64-latest
compression_mode: pixz_x
portage_confdir: /var/tmp/catalyst/releases/weekly/portage/isos

livecd/use:
	fbcon
	ipv6
	livecd
	lvm1
	modules
	ncurses
	nls
	nptl
	pam
	readline
	socks5
	ssl
	static-libs
	unicode
	xml

livecd/packages:
	app-accessibility/brltty
	app-admin/hddtemp
	app-admin/passook
	app-admin/pwgen
	app-admin/syslog-ng
	app-arch/unzip
	app-crypt/gnupg
	app-editors/mg
	app-editors/nano
	# let's bring a vi editor back and use vim instead
	# cause I think it's better :)
	app-editors/vim
	app-misc/screen
	# some people prefer tmux instead
	app-misc/tmux
	# more easily manage a package.use file
	app-portage/flaggie
	app-portage/mirrorselect
	# convenient ncurses interface to enable or disable
	# USE flags system-wide
	app-portage/ufed
	app-text/wgetpaste
	media-gfx/fbgrab
	media-libs/mesa
	net-analyzer/traceroute
	net-dialup/mingetty
	net-dialup/pptpclient
	net-dialup/rp-pppoe
	net-fs/cifs-utils
	net-fs/nfs-utils
	net-irc/irssi
	net-misc/dhcpcd
	net-misc/iputils
	net-misc/ndisc6
	net-misc/ntp
	net-misc/openssh
	net-misc/rdate
	net-misc/rsync
	net-misc/vconfig
	net-proxy/dante
	net-proxy/tsocks
	net-wireless/b43-fwcutter
### Masked (~keywords)
#	net-wireless/bcm43xx-fwcutter
	net-wireless/iw
	net-wireless/wireless-tools
	net-wireless/wpa_supplicant
	sys-apps/busybox
	sys-apps/dmidecode
	sys-apps/ethtool
	sys-apps/fxload
	sys-apps/gptfdisk
	sys-apps/hdparm
	sys-apps/hwsetup
	sys-apps/iproute2
	# kmscon is ~amd64 and HIGHLY experimental
	sys-apps/kmscon
	# yet another way to list system hardware
	sys-apps/lshw
	sys-apps/memtester
	sys-apps/netplug
	sys-apps/pciutils
	sys-apps/sdparm
	sys-apps/usbutils
	sys-block/parted
	sys-block/partimage
	sys-fs/btrfs-progs
	sys-fs/cryptsetup
	sys-fs/dmraid
	sys-fs/dosfstools
	sys-fs/e2fsprogs
	sys-fs/f2fs-tools
	sys-fs/jfsutils
	sys-fs/lsscsi
	sys-fs/lvm2
	sys-fs/mac-fdisk
	sys-fs/mdadm
	sys-fs/multipath-tools
	sys-fs/ntfs3g
	sys-fs/reiserfsprogs
	sys-fs/xfsprogs
	#force rebuild for USE="(-multilib*)"
	sys-libs/glibc
	sys-libs/gpm
	sys-power/acpid
	www-client/links
