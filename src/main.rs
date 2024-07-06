#![allow(non_snake_case)]

use std::process::ExitCode;

use clap::Parser;

mod cli;

fn main() -> ExitCode {
    let args = cli::Args::parse();

    let settings = rustpython_vm::Settings::default()
        .with_path("".to_string())
        .with_path("/Users/muyunxi/Library/Python/3.10/lib/python/site-packages".to_string());

    let interpreter = rustpython::InterpreterConfig::new()
        .settings(settings)
        .init_stdlib()
        .interpreter();

    match args.file {
        Some(f) => {
            println!("File: {}", f);
        },
        None => {
            interpreter.enter(|vm| {
                let scope = vm.new_scope_with_builtins();
                let _ = vm.run_script(scope, "main.py");
            });
        }
    }

    ExitCode::SUCCESS
}
