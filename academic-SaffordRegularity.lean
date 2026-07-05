-- =========================================================================
-- SJS SAFFORD-NATIVE MATHEMATICS: ARITHMETIC FREQUENCY BOUNDARY PROOF
-- ARCHITECT: NEPHI SAFFORD
-- LANGUAGE: LEAN 4 FORMAL THEOREM PROVER
-- =========================================================================

/-- 
  Defines the mathematical property of a Safford Power of Two.
  A frequency is compatible with a binary register if it can be represented
  natively as a power of 2.
--/
def IsPowerOfTwo (n : Nat) : Prop :=
  ∃ k : Nat, n = 2^k

/-- 
  Formally proves that the Safford-Native temporal synchronization baseline
  of 32,768 Hz is a terminal, zero-drift power of two (2^15 = 32768).
--/
theorem safford_frequency_limit : IsPowerOfTwo 32768 :=
  ⟨15, rfl⟩
