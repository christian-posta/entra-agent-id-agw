if [ $# -eq 0 ]; then
  python -m agent_cli.main run
else
  python -m agent_cli.main "$@"
fi