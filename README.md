# ExynosTools Android Layer

Builds an ARM64 Android debug-layer APK for Samsung Xclipse devices.

Target layer: `VK_LAYER_EXYNOSTOOLS_bcn`

Package: `com.wade.exynostools.layer`

The build uses the upstream ExynosTools source and packages the resulting Vulkan compatibility layer as a separate APK. It does not replace `vulkan.samsung.so`, modify the GTA V APK, or modify the system driver.

Run GitHub Actions -> Build ExynosTools Android Layer -> Run workflow. The APK is uploaded as the `ExynosTools-Layer-debug` artifact.
