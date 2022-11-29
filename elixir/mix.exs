defmodule AOC.MixProject do
  use Mix.Project

  def project do
    [
      app: :advent_of_code,
      version: "0.1.0",
      elixir: "~> 1.12",
      start_permanent: Mix.env() == :prod,
      deps: deps(),

      # Docs
      name: "Advent of Code",
      source_url: "https://github.com/gahjelle/advent_of_code/tree/main/elixir",
      homepage_url: "https://github.com/gahjelle/advent_of_code",
      docs: [
        extras: ["README.md"]
      ]
    ]
  end

  # Run "mix help compile.app" to learn about applications.
  def application do
    [
      extra_applications: [:crypto, :logger]
    ]
  end

  # Run "mix help deps" to learn about dependencies.
  defp deps do
    [
      {:benchee, "~> 1.0", only: [:dev, :test]},
      {:credo, "~> 1.6", only: [:dev, :test], runtime: false},
      {:ex_doc, "~> 0.27", only: :dev, runtime: false},
      {:heap, "~> 2.0"},
      {:nimble_parsec, "~> 1.1"},
      {:number, "~> 1.0", only: [:dev, :test]},
      {:statistics, "~> 0.6.2"}
    ]
  end
end
