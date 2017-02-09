package main

import (
	"crypto/md5"
	"fmt"
	"io"
	"os"
	"path"
	"path/filepath"
)

// ファイル名、ファイルサイズ、md5の値を算出する

func computeMd5(filePath string) ([]byte, error) {
	var result []byte
	file, err := os.Open(filePath)
	if err != nil {
		return result, err
	}
	defer file.Close()

	hash := md5.New()
	if _, err := io.Copy(hash, file); err != nil {
		return result, err
	}

	return hash.Sum(result), nil
}

func fileSize(filePath string) (int64, error) {
	file, err := os.Open(filePath)
	if err != nil {
		return -1, err
	}
	defer file.Close()
	fileinfo, staterr := file.Stat()
	if staterr != nil {
		return -1, staterr
	}
	return fileinfo.Size(), nil
}

func printFileInfo(filePath string) {
	md5, md5Err := computeMd5(filePath)
	if md5Err != nil {
		fmt.Printf("md5Err: %v\n", md5Err)
		return
	}
	size, sizeErr := fileSize(filePath)
	if sizeErr != nil {
		fmt.Printf("sizeErr: %v\n", sizeErr)
		return
	}
	fileName := path.Base(filepath.ToSlash(filePath))
	fmt.Printf("------------------\n")
	fmt.Printf("fileName: %v\n", fileName)
	fmt.Printf("md5hash: %x\n", md5)
	fmt.Printf("size: %v byte\n", size)
}

func main() {
	for i, p := range os.Args {
		if i == 0 {
			continue
		}
		filePaths, globErr := filepath.Glob(p)
		if globErr != nil {
			fmt.Println(globErr)
			continue
		}
		for _, f := range filePaths {
			printFileInfo(f)
		}
	}
}
