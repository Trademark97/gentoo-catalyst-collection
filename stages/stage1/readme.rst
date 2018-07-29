Stage 1 Tarballs
===============
These are stage1 tarballs that I have built using Catalyst.

What are Stage 1 tarballs?
--------------------------
Stage 1 tarballs contain the minimal set of files necessary to bootstrap the system. When you run the bootstrapping
process, you rebuild the toolchain with the **CFLAGS/CXXFLAGS** and/or **LDFLAGS** defined in your *make.conf* file.
This is functionally equivalent to what is provided by a Stage 2 tarball.

Why would I use a Stage 1 tarball?
----------------------------------
There are a couple of reasons that you might wish to use a Stage 1 tarball as opposed to a more *"normal"* Stage 3 tarball.
You can completely compile the system from scratch, which may or may not produce noticeable differences in performance.
You might gain a greater understanding of the work necessary to build a Linux install truly from scratch (as much of the work
done in a Gentoo Stage 1 build is quite similar to that which is necessary to be done during the compilation stage of the
**Linux from Scratch** handbook). Or, you might wish to experience what used to be the normal install in the "old days" of
Gentoo.

Why are you hosting your stage tarballs on Google Drive?
--------------------------------------------------------
This is a temporary workaround to a restriction imposed by Github, which has a hard limit of 100MiB (stage tarballs can
be, and most often are, much larger than that). Once I complete the transition to Gitlab, the tarballs will be directly
hosted on the repository itself.
