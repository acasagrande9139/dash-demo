def header():
    map = [
        ("_id", "ID"),
        ("cpeid", "CPEID"),
        ("metadata.CLI", "CLI"),
        ("metadata.PRV.VOIP_MBS.1.USERNAME", "VoIP DN"),
        ("props.DI.M", "Manufacturer"),
        ("props.DI.PC", "ProductClass"),
        ("props.DI.HV", "HardwareVersion"),
        ("props.DI.SV", "SoftwareVersion"),
        ("props.DI.SN", "SerialNumber"),
        ("metadata.REGIONE", "REGIONE"),
        ("metadata.PROVINCIA", "PROVINCIA"),
        ("metadata.COMUNE", "COMUNE"),
        ("metadata.TECNOLOGIA", "TECNOLOGIA"),
        ("metadata.APPARATO", "APPARATO"),
        ("metadata.PRV.DSLAM", "DSLAM"),
        ("metadata.PRV.PRV_DATE", "Provisioning Date"),
        ("metadata.PRV.ACTIVATION_ID", "Activation ID"),
        ("mode_props.kr.KPI.AG.sWAN", "Line Stability"),
        ("mode_props.kr.KPI.AG.SESWAN", "Line Quality"),
    ]
    return map


def create_color_map(arr):
    # Create an array of base colors
    import numpy as np
    color = np.array(["rgb(255, 255, 255)"] * arr.shape[0])
    # Adjust it according to thresholds
    color[arr < 5000] = "rgb(255, 0, 0)"
    color[(arr >= 5000) & (arr < 10000)] = "rgb(255, 165, 0)"
    color[(arr >= 10000) & (arr < 15000)] = "rgb(255, 255, 0)"
    color[(arr >= 15000) & (arr < 20000)] = "rgb(144, 238, 144)"
    color[arr >= 20000] = "rgb(0, 100, 0)"
    return color


if __name__ == "__main__":
    pass
