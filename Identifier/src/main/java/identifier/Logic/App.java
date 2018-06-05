package identifier.Logic;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.domain.EntityScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.data.jpa.repository.config.EnableJpaRepositories;

import java.io.File;

@SpringBootApplication
@ComponentScan(basePackages = "identifier")
@EntityScan("identifier.Repository.Entities")
@EnableJpaRepositories("identifier.Repository")
public class App {
    public static void main(String[] args) {
        SpringApplication.run(App.class, args);
    }
}
