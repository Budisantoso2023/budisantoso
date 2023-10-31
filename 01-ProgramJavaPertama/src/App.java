public class App {
    public static void main(String[] args) throws Exception {
    // Program Biodata Mahasiswa
    // deklarasi variable
    String nama;
    String nim;
    String tgl_lahir;
    String alamat;
    float berat_badan;
    float tinggi_badan;

    // mengisi variable
    nama = "Budi";
    nim  = "23241046";
    tgl_lahir = "08 mei 2005";
    alamat = "lombok timur No. 78";
    berat_badan = 50.5f;
    tinggi_badan = 170.3f;

    // cetak Biodata 
    System.out.println("===================");
    System.out.println("Nama : " + nama);
    System.out.println("NIM : " + nim);
    System.out.println(" Tanggal Lahir : " + tgl_lahir);
    System.out.println("Alamat :" + alamat);
    System.out.println("Berat Badan :" + berat_badan);
    System.out.println("Tinggi Badan :" + tinggi_badan);
    System.out.println("===================");

    }
}
