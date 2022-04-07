package myPack;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class GeneratorVertebraeFromCurves84423 {

	public GeneratorVertebraeFromCurves84423() {
	}

	public String file2Line(String filename) throws IOException {

		File inputFile = new File("farrago.txt");
		File outputFile = new File("outagain.txt");
		FileReader in = new FileReader(inputFile);
		FileWriter out = new FileWriter(outputFile);
		int c;
		while ((c = in.read()) != -1)
			out.write(c);
		in.close();
		out.close();

		return "";
	}

	public static void main(String[] args) {

	}

}
