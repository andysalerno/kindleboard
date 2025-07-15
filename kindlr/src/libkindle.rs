use std::{error::Error, path::Path, process::Command};

/// Displays a PNG image on a Kindle device using the `eips` command-line tool.
pub fn display_png(path: &Path) -> Result<(), Box<dyn Error>> {
    let status = Command::new("eips")
        .arg("-g")
        .arg(path)
        .arg("-w")
        .arg("gc16")
        .status()
        .map_err(|e| format!("Failed to execute eips: {e}"))?;

    if !status.success() {
        return Err(format!("eips exited with non-zero status: {status}").into());
    }

    Ok(())
}

pub fn wget(url: &str, output: &Path) -> Result<(), Box<dyn Error>> {
    let status = Command::new("wget")
        .arg(url)
        .arg("-O")
        .arg(output)
        .status()
        .map_err(|e| format!("Failed to execute wget: {e}"))?;

    if !status.success() {
        return Err(format!("wget exited with non-zero status: {status}").into());
    }

    Ok(())
}
