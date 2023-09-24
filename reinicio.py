import subprocess

def restart_pcscd():
    try:
        subprocess.run(['sudo', 'systemctl', 'restart', 'pcscd'], check=True)
        print('pcscd service restarted successfully.')
    except subprocess.CalledProcessError as e:
        print(f'Error: Failed to restart pcscd service. {e}')

# Llama a la función para reiniciar pcscd
restart_pcscd()
