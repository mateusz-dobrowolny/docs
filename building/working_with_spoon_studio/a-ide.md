## Working with Spoon Studio

Spoon Studio is a desktop application that allows you to convert any Windows application into a self-contained virtual application. Virtual applications can be delivered as standalone executables, MSIs or Spoon images. 

The GUI allows users to easily edit complex configurations for applications that may require complicated settings. Whereas Spoon's command line tool builds images from containers, Spoon Studio uses static XML files (**.xappl**) to build images. More information about the XAPPL file format is available in the [XAPPL reference](/docs/reference/xappl).

Once created with Spoon Studio, the command-line interface builds these XAPPL files into images that you can push to the Spoon Hub. Click [here](/docs/building/working-with-images) for a specific example.

Spoon Studio also provides two unique methods for creating images and virtual applications:

1. **Desktop scan for installed applications**: This option will scan your desktop for installed applications and build an image or virtual application using content and settings from the desktop.

2. **Snapshot an application or component**: In this method, snapshots capture the system state before and after an application is installed. Based on the observed system changes, the virtual application settings are automatically configured. This method is ideal for virtualizing off-the-shelf applications or ones that use complex MSI installer packages that would be incompatible with the command-line interface.

Spoon Studio offers a user interface to manage custom images and virtual applications as well as additional creation methods not available in the command-line interface.

<!--TODO: add a brief section on when you would want to use Spoon Studio vs. the CLI -->

#### System requirements and download

Spoon Studio runs on any Windows operating system, including systems running within VMware and Microsoft hardware virtualization and hypervisor environments. Spoon Studio has limited support for the Windows Preinstallation Environment (WinPE), though certain applications (depending on operating system features unavailable in WinPE) may not function properly.

Spoon Studio supports both 32- and 64-bit applications. Both 32-bit (under 32-bit mode) and 64-bit executables can be run on x64-based platforms.

**Note:** Spoon Studio does not support creation of 16-bit executables. To run 16-bit DOS applications, virtualize an appropriate emulator with the application and launch the application through the emulator.

Download a free 30-day trial [here](/studio) or try the free, [express version](http://turbo.net/studio-express). 