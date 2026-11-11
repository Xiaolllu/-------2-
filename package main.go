package main

import (
	"bufio"
	"fmt"
	"math/rand"
	"os"
	"strconv"
	"strings"
	"time"
)

func main() {
	rand.Seed(time.Now().UnixNano())

	target := rand.Intn(100) + 1
	reader := bufio.NewReader(os.Stdin)

	fmt.Println("欢迎来到猜数字游戏！")
	fmt.Println("我已经想好了一个 1 到 100 之间的数字。")

	for attempts := 1; ; attempts++ {
		fmt.Printf("\n第 %d 次猜测，请输入数字：", attempts)

		input, err := reader.ReadString('\n')
		if err != nil {
			fmt.Println("读取输入失败：", err)
			return
		}

		guess, err := strconv.Atoi(strings.TrimSpace(input))
		if err != nil {
			fmt.Println("请输入有效的整数。")
			continue
		}

		switch {
		case guess < 1 || guess > 100:
			fmt.Println("请输入 1 到 100 之间的数字。")
		case guess < target:
			fmt.Println("太小了！")
		case guess > target:
			fmt.Println("太大了！")
		default:
			fmt.Printf("恭喜你，答对了！一共猜了 %d 次。\n", attempts)
			return
		}
	}
}
