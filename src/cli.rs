use clap::Parser;

#[derive(Parser, Debug)]
#[command(name = "CAIE Code")]
#[command(author = "Iewnfod")]
#[command(version = "0.2.0")]
#[command(about = "An interpreter for Cambridge International Education Pseudocode", long_about = "None")]
pub struct Args {
	/// The file to run
	pub file: Option<String>,
}
