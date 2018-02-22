Name: nvidia-container-runtime-hook
Version: %{version}
Release: %{release}
Group: Development Tools

Vendor: NVIDIA CORPORATION
Packager: NVIDIA CORPORATION <cudatools@nvidia.com>

Summary: NVIDIA container runtime hook
URL: https://github.com/NVIDIA/nvidia-container-runtime
License: BSD

Source0: nvidia-container-runtime-hook
Source1: config.toml
Source2: LICENSE

Obsoletes: nvidia-container-runtime < 2.0.0
Requires: libnvidia-container-tools >= 0.1.0, libnvidia-container-tools < 2.0.0

%description
Provides a OCI hook to enable GPU support in containers.

%prep
cp %{SOURCE0} %{SOURCE1} %{SOURCE2} .

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 -t %{buildroot}%{_bindir} nvidia-container-runtime-hook
mkdir -p %{buildroot}/etc/nvidia-container-runtime
install -m 644 -t %{buildroot}/etc/nvidia-container-runtime config.toml

%files
%license LICENSE
%{_bindir}/nvidia-container-runtime-hook
/etc/nvidia-container-runtime/config.toml

%changelog
