// SaDsEc_001/challenge_001 Solution Created By Cne3Rd

package main

import (
	"fmt"
	"os"
	"bufio"
	"io/ioutil"
	"crypto/sha256"
	"encoding/hex"
)

var (
    targetFileName = "sadsecCTF"
	targetHash = ""
)

func main() {
    targetHash = openfile(targetFileName)
   // fmt.Println(targetHash)
	file, err := os.Open("usernames.txt")
	if err != nil {
		fmt.Println(err)
	}

	scan := bufio.NewScanner(file)

	
	for scan.Scan() {
		word := scan.Text()
		fhword, w := checkHash(word)
	//	fmt.Println(fhword, w)
		if fhword  == targetHash {
		    fmt.Println(fhword, w)
		}

		//fmt.Println(w)
	}
}

func checkHash(word string) (string, string) {
	csv := sha256.Sum256([]byte(word))
	newCheckSum := make([]byte, 0)
	for _, v := range csv {
	    newCheckSum = append(newCheckSum, v)
	 }

	 return hex.EncodeToString(newCheckSum), word
}

func openfile(name string) string {
    res, err := ioutil.ReadFile(name)
    if err != nil {
    	fmt.Println(err)
    }
    return string(res)
}



