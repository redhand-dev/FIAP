public class NANOCAP03EX01_conta {
	
	int numero;
	
	int agencia;
	
	double saldo;
	
	public Conta(){
		
	}
	
	public Conta(int numero, int agencia, double saldo){
		this.numero = numero;
		this.agencia = agencia;
		this.saldo = saldo;
	}
	
	public void depositar(double valor){
		this.saldo += valor;
	}
	
	public void retirar(double valor){
		this.saldo -= valor;
	}
	
	public double verificarSaldo(){
		return saldo;
	}
}