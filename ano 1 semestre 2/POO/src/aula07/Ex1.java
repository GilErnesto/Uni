package aula07;

public class Ex1 {
    abstract class Forma {
        protected String cor;

        public Forma(String cor) {
            this.cor = cor;
        }

        public String getCor() {
            return cor;
        }

        public void setCor(String cor) {
            this.cor = cor;
        }

        public abstract double area();
        public abstract double perimetro();

        @Override
        public boolean equals(Object obj) {
            if (this == obj) return true;
            if (obj == null || getClass() != obj.getClass()) return false;
            Forma forma = (Forma) obj;
            return cor.equals(forma.cor);
        }
    }

    public class Circle extends Forma {
        private float raio;

        public Circle(float raio, String cor) {
            super(cor);
            if (raio <= 0) throw new IllegalArgumentException("O raio deve ser positivo.");
            this.raio = raio;
        }

        public float getRaio() {
            return raio;
        }

        public void setRaio(float raio) {
            if (raio <= 0) throw new IllegalArgumentException("O raio deve ser positivo.");
            this.raio = raio;
        }

        @Override
        public double area() {
            return Math.PI * raio * raio;
        }

        @Override
        public double perimetro() {
            return 2 * Math.PI * raio;
        }

        @Override
        public String toString() {
            return String.format("Círculo %s com raio: %.2f", cor, raio);
        }
    }


    class Triangulo extends Forma {
        private float lado1, lado2, lado3;

        public Triangulo(float lado1, float lado2, float lado3, String cor) {
            super(cor);
            if (!isValidTriangle(lado1, lado2, lado3)) 
                throw new IllegalArgumentException("Os lados não formam um triângulo válido.");
            this.lado1 = lado1;
            this.lado2 = lado2;
            this.lado3 = lado3;
        }

        private boolean isValidTriangle(float lado1, float lado2, float lado3) {
            return lado1 + lado2 > lado3 && lado1 + lado3 > lado2 && lado2 + lado3 > lado1 &&
                   lado1 > 0 && lado2 > 0 && lado3 > 0;
        }

        @Override
        public double area() {
            double s = (lado1 + lado2 + lado3) / 2.0;
            return Math.sqrt(s * (s - lado1) * (s - lado2) * (s - lado3));
        }

        @Override
        public double perimetro() {
            return lado1 + lado2 + lado3;
        }

        @Override
        public String toString() {
            return String.format("Triângulo %s com lados: %.2f, %.2f, %.2f", cor, lado1, lado2, lado3);
        }
    }
    class Retangulo extends Forma {
        private float base;
        private float altura;

        public Retangulo(float base, float altura, String cor) {
            super(cor);
            if (base <= 0 || altura <= 0) 
                throw new IllegalArgumentException("Base e altura devem ser positivos.");
            this.base = base;
            this.altura = altura;
        }

        @Override
        public double area() {
            return base * altura;
        }

        @Override
        public double perimetro() {
            return 2 * (base + altura);
        }

        @Override
        public String toString() {
            return String.format("Retângulo %s com base: %.2f e altura: %.2f", cor, base, altura);
        }
    }

    public static void main(String[] args) {
        Ex1 ex1 = new Ex1();
        Forma circle = ex1.new Circle(5, "vermelho");
        Forma triangulo = ex1.new Triangulo(3, 4, 5, "azul");
        Forma retangulo = ex1.new Retangulo(4, 6, "verde");

        System.out.println(circle);
        System.out.println("Área: " + circle.area());
        System.out.println("Perímetro: " + circle.perimetro());

        System.out.println(triangulo);
        System.out.println("Área: " + triangulo.area());
        System.out.println("Perímetro: " + triangulo.perimetro());

        System.out.println(retangulo);
        System.out.println("Área: " + retangulo.area());
        System.out.println("Perímetro: " + retangulo.perimetro());

   
        Forma circle2 = ex1.new Circle(3, "vermelho");
        System.out.println("\nCirculos iguais? " + circle.equals(circle2)); 
        Forma circle3 = ex1.new Circle(5, "azul");
        System.out.println("Circulos iguais? " + circle.equals(circle3)); 
    }
}