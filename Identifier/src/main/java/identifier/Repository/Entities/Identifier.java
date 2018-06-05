package identifier.Repository.Entities;

import javax.persistence.*;

@Entity
public class Identifier {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;
    private String nonce;

    protected  Identifier() {}

    public Identifier(String nonce) {
        this.nonce = nonce;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getNonce() {
        return nonce;
    }

    public void setNonce(String nonce) {
        this.nonce = nonce;
    }
}
