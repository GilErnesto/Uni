package aula04;

public class Formas {

    class Circle {
        private float raio;

        public Circle(float raio) {
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

        public double area() {
            return Math.PI * raio * raio;
        }

        public double perimetro() {
            return 2 * Math.PI * raio;
        }

        @Override
        public String toString() {
            return String.format("Círculo com raio: %.2f", raio);
        }

        @Override
        public boolean equals(Object obj) {
            if (this == obj) return true;
            if (obj == null || getClass() != obj.getClass()) return false;
            Circle circle = (Circle) obj;
            return Float.compare(circle.raio, raio) == 0;
        }
    }

    class Triangulo {
        private float lado1;
        private float lado2;
        private float lado3;

        public Triangulo(float lado1, float lado2, float lado3) {
            if (lado1 <= 0 || lado2 <= 0 || lado3 <= 0) throw new IllegalArgumentException("Os lados devem ser positivos.");
            if (!isValidTriangle(lado1, lado2, lado3)) throw new IllegalArgumentException("Os lados não satisfazem a desigualdade triangular.");
            this.lado1 = lado1;
            this.lado2 = lado2;
            this.lado3 = lado3;
        }

        public float getLado1() {
            return lado1;
        }

        public void setLado1(float lado1) {
            if (lado1 <= 0) throw new IllegalArgumentException("O lado deve ser positivo.");
            if (!isValidTriangle(lado1, lado2, lado3)) throw new IllegalArgumentException("Os lados não satisfazem a desigualdade triangular.");
            this.lado1 = lado1;
        }

        public float getLado2() {
            return lado2;
        }

        public void setLado2(float lado2) {
            if (lado2 <= 0) throw new IllegalArgumentException("O lado deve ser positivo.");
            if (!isValidTriangle(lado1, lado2, lado3)) throw new IllegalArgumentException("Os lados não satisfazem a desigualdade triangular.");
            this.lado2 = lado2;
        }

        public float getLado3() {
            return lado3;
        }

        public void setLado3(float lado3) {
            if (lado3 <= 0) throw new IllegalArgumentException("O lado deve ser positivo.");
            if (!isValidTriangle(lado1, lado2, lado3)) throw new IllegalArgumentException("Os lados não satisfazem a desigualdade triangular.");
            this.lado3 = lado3;
        }

        private boolean isValidTriangle(float lado1, float lado2, float lado3) {
            return lado1 + lado2 > lado3 && lado1 + lado3 > lado2 && lado2 + lado3 > lado1;
        }

        public double area() {
            double s = (lado1 + lado2 + lado3) / 2.0;
            return Math.sqrt(s * (s - lado1) * (s - lado2) * (s - lado3));
        }

        public double perimetro() {
            return lado1 + lado2 + lado3;
        }

        @Override
        public String toString() {
            return String.format("Triângulo com lados: %.2f, %.2f, %.2f", lado1, lado2, lado3);
        }

        @Override
        public boolean equals(Object obj) {
            if (this == obj) return true;
            if (obj == null || getClass() != obj.getClass()) return false;
            Triangulo triangulo = (Triangulo) obj;
            return Float.compare(triangulo.lado1, lado1) == 0 &&
                   Float.compare(triangulo.lado2, lado2) == 0 &&
                   Float.compare(triangulo.lado3, lado3) == 0;
        }
    }

    class Retangulo {
        private float base;
        private float altura;

        public Retangulo(float base, float altura) {
            if (base <= 0 || altura <= 0) throw new IllegalArgumentException("Base e altura devem ser positivos.");
            this.base = base;
            this.altura = altura;
        }

        public float getBase() {
            return base;
        }

        public void setBase(float base) {
            if (base <= 0) throw new IllegalArgumentException("A base deve ser positiva.");
            this.base = base;
        }

        public float getAltura() {
            return altura;
        }

        public void setAltura(float altura) {
            if (altura <= 0) throw new IllegalArgumentException("A altura deve ser positiva.");
            this.altura = altura;
        }

        public double area() {
            return base * altura;
        }

        public double perimetro() {
            return 2 * (base + altura);
        }

        @Override
        public String toString() {
            return String.format("Retângulo com base: %.2f e altura: %.2f", base, altura);
        }

        @Override
        public boolean equals(Object obj) {
            if (this == obj) return true;
            if (obj == null || getClass() != obj.getClass()) return false;
            Retangulo retangulo = (Retangulo) obj;
            return Float.compare(retangulo.base, base) == 0 &&
                   Float.compare(retangulo.altura, altura) == 0;
        }
    }

    public static void main(String[] args) {
        Formas ex1 = new Formas();
        Circle circle = ex1.new Circle(5);
        Triangulo triangulo = ex1.new Triangulo(3, 4, 5);
        Retangulo retangulo = ex1.new Retangulo(4, 6);

        System.out.println(circle);
        System.out.println("Área: " + circle.area());
        System.out.println("Perímetro: " + circle.perimetro());

        System.out.println(triangulo);
        System.out.println("Área: " + triangulo.area());
        System.out.println("Perímetro: " + triangulo.perimetro());

        System.out.println(retangulo);
        System.out.println("Área: " + retangulo.area());
        System.out.println("Perímetro: " + retangulo.perimetro());
    }
}